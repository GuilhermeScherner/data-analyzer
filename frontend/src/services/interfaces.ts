export interface GetAnalyticsResponse {
  id: number
  name: string
  mrr: object
  churn: object
  date: string
}

export interface GetListAnalyticsResponse {
  id: number
  name: string
  date: string
}

export interface UploadFileResponse {
  id: number
}
