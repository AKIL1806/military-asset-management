import React, { useEffect, useState } from "react";
import AssetList from "../components/AssetList";
import type { Asset } from "../services/assetService";
import { fetchAssets } from "../services/assetService";

const Dashboard: React.FC = () => {
  const [assets, setAssets] = useState<Asset[]>([]);

  useEffect(() => {
    fetchAssets()
      .then((data) => setAssets(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <AssetList assets={assets} />
    </div>
  );
};

export default Dashboard;
