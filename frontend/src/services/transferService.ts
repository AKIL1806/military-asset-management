const API_URL = "http://localhost:8000/api/v1/transfers";

export interface Transfer {
  id: number;
  asset_id: number;
  from_base_id: number;
  to_base_id: number;
  quantity: number;
  transfer_date: string;
  // Add other fields if any
}

export async function fetchTransfers(): Promise<Transfer[]> {
  const response = await fetch(API_URL);
  if (!response.ok) {
    throw new Error(`Failed to fetch transfers: ${response.statusText}`);
  }
  return response.json();
}
