import type { SubjectData } from './SubjectData'
import type { OfficeData } from './OfficeData'

interface TeacherData {
  id: number
  name: string
  photo_file: string
  office: OfficeData
  subjects: SubjectData[]
}

export type { TeacherData }
