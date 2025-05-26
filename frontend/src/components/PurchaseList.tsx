import React from "react";
import type { Purchase } from "../services/purchaseService";

interface PurchaseListProps {
  purchases: Purchase[];
}

const PurchaseList: React.FC<PurchaseListProps> = ({ purchases }) => {
  if (purchases.length === 0) return <p>No purchases found.</p>;

  return (
    <div>
      {purchases.map((purchase) => (
        <div key={purchase.id} className="border p-4 mb-2 rounded shadow">
          <p><strong>Purchase ID:</strong> {purchase.id}</p>
          <p><strong>Asset ID:</strong> {purchase.asset_id}</p>
          <p><strong>Base ID:</strong> {purchase.base_id}</p>
          <p><strong>Quantity:</strong> {purchase.quantity}</p>
          {purchase.notes && <p><strong>Notes:</strong> {purchase.notes}</p>}
          <p><strong>Purchase Date:</strong> {new Date(purchase.purchase_date).toLocaleString()}</p>
        </div>
      ))}
    </div>
  );
};

export default PurchaseList;
