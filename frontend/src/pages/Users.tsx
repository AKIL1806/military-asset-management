import React, { useEffect, useState } from "react";
import type { User } from "../services/userService";
import { fetchUsers } from "../services/userService";

const Users: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchUsers()
      .then(setUsers)
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <p className="text-red-500">Error: {error}</p>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Users</h1>
      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <ul className="space-y-2">
          {users.map((user) => (
            <li key={user.id} className="border p-4 rounded shadow">
              <p><b>Username:</b> {user.username}</p>
              <p><b>Role:</b> {user.role}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Users;
