const API_URL = "http://localhost:8000/api/v1/purchases";

export interface Purchase {
  id: number;
  asset_id: number;
  base_id: number;
  quantity: number;
  notes?: string;
  purchased_by?: number;
  purchase_date: string; // ISO string
}

export interface PurchaseCreate {
  asset_id: number;
  base_id: number;
  quantity: number;
  notes?: string;
  purchased_by?: number;
}

export async function fetchPurchases(): Promise<Purchase[]> {
  const response = await fetch(API_URL);
  if (!response.ok) {
    throw new Error(`Failed to fetch purchases: ${response.statusText}`);
  }
  return response.json();
}

export async function createPurchase(purchase: PurchaseCreate): Promise<Purchase> {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(purchase),
  });
  if (!response.ok) {
    throw new Error(`Failed to create purchase: ${response.statusText}`);
  }
  return response.json();
}
