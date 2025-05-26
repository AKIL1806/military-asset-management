const API_URL = "http://localhost:8000/api/v1/users";

export interface User {
  id: number;
  username: string;
  role: string;
  // Add other fields if any
}

export async function fetchUsers(): Promise<User[]> {
  const response = await fetch(API_URL);
  if (!response.ok) {
    throw new Error(`Failed to fetch users: ${response.statusText}`);
  }
  return response.json();
}
