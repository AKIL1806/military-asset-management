import React, { useEffect, useState } from "react";
import AssetList from "../components/AssetList";
import AssetForm from "../components/AssetForm";
import type { Asset } from "../services/assetService";
import { fetchAssets } from "../services/assetService";

const Dashboard: React.FC = () => {
  const [assets, setAssets] = useState<Asset[]>([]);

  useEffect(() => {
    fetchAssets()
      .then(setAssets)
      .catch((err) => console.error(err));
  }, []);

  const handleAddAsset = (newAsset: Asset) => {
    setAssets((prev) => [...prev, newAsset]);
  };

  return (
    <div>
      <h1>Dashboard</h1>
      <AssetForm onAdd={handleAddAsset} />
      <AssetList assets={assets} />
    </div>
  );
};

export default Dashboard;
