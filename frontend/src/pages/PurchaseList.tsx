import React, { useEffect, useState } from "react";
import { fetchPurchases } from "../services/purchaseService";
import type { Purchase } from "../services/purchaseService";
import PurchaseList from "../components/PurchaseList";

const PurchaseListPage: React.FC = () => {
  const [purchases, setPurchases] = useState<Purchase[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchPurchases()
      .then(setPurchases)
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <p className="text-red-500">Error: {error}</p>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Purchases</h1>
      <PurchaseList purchases={purchases} />
    </div>
  );
};

export default PurchaseListPage;
