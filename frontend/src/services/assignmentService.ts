const API_URL = "http://localhost:8000/api/v1/assignments";

export interface Assignment {
  id: number;
  asset_id: number;
  assigned_to: string;
  quantity: number;
  date: string;
  expended: boolean;
}

export async function fetchAssignments(): Promise<Assignment[]> {
  const response = await fetch(API_URL);
  if (!response.ok) {
    throw new Error(`Failed to fetch assignments: ${response.statusText}`);
  }
  return response.json();
}
