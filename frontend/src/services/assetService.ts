const API_BASE_URL = 'http://localhost:8000/api';

export async function fetchAssets() {
  const response = await fetch(`${API_BASE_URL}/assets`);
  if (!response.ok) {
    throw new Error('Failed to fetch assets');
  }
  return response.json();
}
