export interface Municipality {
  id: string;
  name: string;
  reading: string;
  isCompleted: boolean;
  visitDate?: Date;
  photos: string[];
  notes: string;
}

export interface ProgressStats {
  completed: number;
  total: number;
  percentage: number;
}