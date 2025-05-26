import React, { useEffect, useState } from "react";
import type { Asset } from "../services/assetService";
import { fetchAssets } from "../services/assetService";
import AssetList from "../components/AssetList";

const AssetListPage: React.FC = () => {
  const [assets, setAssets] = useState<Asset[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchAssets()
      .then((data: Asset[]) => setAssets(data))
      .catch((err: Error) => setError(err.message));
  }, []);

  if (error) return <p className="text-red-500">Error: {error}</p>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Assets</h1>
      <AssetList assets={assets} />
    </div>
  );
};

export default AssetListPage;
