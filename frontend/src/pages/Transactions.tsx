import React, { useEffect, useState } from "react";
import { fetchTransfers, type Transfer } from "../services/transferService";
import { fetchAssignments, type Assignment } from "../services/assignmentService";

const Transactions: React.FC = () => {
  const [transfers, setTransfers] = useState<Transfer[]>([]);
  const [assignments, setAssignments] = useState<Assignment[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([fetchTransfers(), fetchAssignments()])
      .then(([tr, as]) => {
        setTransfers(tr);
        setAssignments(as);
      })
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <p className="text-red-500">Error: {error}</p>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Transactions</h1>

      <h2 className="text-xl font-semibold mt-4 mb-2">Transfers</h2>
      {transfers.length === 0 ? (
        <p>No transfers found.</p>
      ) : (
        <ul>
          {transfers.map((t) => (
            <li key={t.id} className="border p-3 mb-2 rounded shadow">
              <p><b>Asset ID:</b> {t.asset_id}</p>
              <p><b>From Base:</b> {t.from_base_id}</p>
              <p><b>To Base:</b> {t.to_base_id}</p>
              <p><b>Quantity:</b> {t.quantity}</p>
              <p><b>Date:</b> {new Date(t.transfer_date).toLocaleString()}</p>
            </li>
          ))}
        </ul>
      )}

      <h2 className="text-xl font-semibold mt-6 mb-2">Assignments</h2>
      {assignments.length === 0 ? (
        <p>No assignments found.</p>
      ) : (
        <ul>
          {assignments.map((a) => (
            <li key={a.id} className="border p-3 mb-2 rounded shadow">
              <p><b>Asset ID:</b> {a.asset_id}</p>
              <p><b>Assigned To:</b> {a.assigned_to}</p>
              <p><b>Quantity:</b> {a.quantity}</p>
              <p><b>Date:</b> {a.date}</p>
              <p><b>Expended:</b> {a.expended ? "Yes" : "No"}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Transactions;
