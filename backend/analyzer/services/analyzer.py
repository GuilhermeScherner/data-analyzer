from typing import Any, Dict, List
import json
import pandas as pd
import numpy as np
from fastapi import UploadFile

from analyzer.db.mappings import File
from analyzer.services.base import BaseService
from analyzer.services.models import analyzer as analyzer_models


class AnalyzerService(BaseService):
    """Create service analyzer."""

    async def upload_file_service(
        self,
        file: UploadFile,
    ) -> analyzer_models.AnalyzerCreateResponse:
        """
        Upload file.

        :param file: file.
        :return: Id of the file.
        """
        file.file.seek(0)
        df = self._format_data(pd.read_csv(file.file, sep=","))
        df["diff_month"] = np.where(
            df["data cancelamento"].notnull(),
            ((df["data cancelamento"] - df["data início"]) / pd.Timedelta(days=30)),
            ((df["próximo ciclo"] - df["data início"]) / pd.Timedelta(days=30)),
        ).astype(int)

        mrr = self._create_mrr(df.copy())
        churn = self._create_churn(df.copy())
        create_model = self._create_model(mrr, churn, file)

        return analyzer_models.AnalyzerCreateResponse(id=create_model["id"])

    async def get_analyzer_service(
        self,
        id: int,
    ) -> analyzer_models.AnalyzerGetResponse:
        """
        Get analyzer.

        :param id: id of the file.
        :return: analyzer.
        """
        with self.uow as uow:
            file = uow.file.get(id)
            if(file is None):
                return None
            file_json = file.to_dict()
            file_json["mrr"] = json.loads(file_json["mrr"])
            file_json["churn"] = json.loads(file_json["churn"])
        return analyzer_models.AnalyzerGetResponse(**file_json)

    async def get_analyzer_list_service(
        self,
    ) -> List[analyzer_models.AnalyzerListGetResponse]:
        """
        Get analyzer list.

        :return: analyzer list.
        """
        with self.uow as uow:
            files = uow.file.get_all()
        return [analyzer_models.AnalyzerListGetResponse(**file.to_dict()) for file in files]

    def _create_mrr(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Create model.

        :param df: dataframe.
        :return: analyzer dict.
        """
        month_df = pd.DataFrame()

        for index, row in df.iterrows():
            for value_month in range(row["diff_month"]):
                date = row["data início"] + pd.DateOffset(months=value_month)
                new_col_name = date.strftime("%m/%y")
                month_df.loc[index, new_col_name] = row["valor"] / row["diff_month"]

        month_df = month_df[
            sorted(
                month_df.columns,
                key=lambda val: pd.to_datetime(val, format="%m/%y"),
            )
        ]
        return month_df.sum().round(2).to_json(indent=2)

    def _create_churn(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Create model.

        :param df: dataframe.
        :return: analyzer dict.
        """
        df['initial_month'] = df['data início'].dt.to_period('M')
        churn = df.groupby('initial_month').agg(
            initial=('quantidade cobranças', 'sum'),
            canceled=('data cancelamento', 'count')
        )
        churn['canceled'].fillna(0, inplace=True)
        churn['churn_rate'] = churn['canceled'] / churn['initial']
        churn = churn[churn['churn_rate'] != 0]

        return churn['churn_rate'].to_json(indent=2)

    def _create_model(
        self, data_mrr: Dict[str, Any], data_churn: Dict[str, Any], file: UploadFile
    ) -> Dict[str, Any]:
        """
        Create model.

        :param data_mrr: data mrr.
        :param data_churn: data churn.
        :param file: file.
        :return: analyzer model.
        """
        with self.uow as uow:
            file_mapping = File(
                **{"name": file.filename, "mrr": data_mrr, "churn": data_churn}
            )
            result = uow.file.add(file_mapping)
        return result.to_dict()

    def _format_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Format data.

        :param df: dataframe.
        :return: dataframe.
        """
        new_df = df.copy()
        new_df["valor"] = new_df["valor"].str.replace(",", ".")
        new_df["valor"] = new_df["valor"].astype(float)
        new_df["data início"] = pd.to_datetime(
            new_df["data início"],
            format="%m/%d/%y %H:%M",
            errors="coerce",
        )
        new_df["próximo ciclo"] = pd.to_datetime(
            new_df["próximo ciclo"],
            format="%m/%d/%Y",
            errors="coerce",
        )
        new_df = new_df.dropna(subset=["próximo ciclo"])
        new_df["mes"] = new_df["data início"].dt.to_period("M")
        new_df["data cancelamento"] = pd.to_datetime(
            new_df["data cancelamento"],
            format="%m/%d/%y %H:%M",
            errors="coerce",
        )
        new_df["quantidade cobranças"] = new_df["quantidade cobranças"].astype(int)
        new_df["cobrada a cada X dias"] = new_df["cobrada a cada X dias"].astype(int)
        return new_df
