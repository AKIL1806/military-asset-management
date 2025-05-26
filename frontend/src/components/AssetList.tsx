import React from "react";
import type { Asset } from "../services/assetService";

interface AssetListProps {
  assets: Asset[];  // ensure this is always an array
}

const AssetList: React.FC<AssetListProps> = ({ assets }) => {
  if (!assets || assets.length === 0) {
    return <p>No assets found.</p>;
  }

  return (
    <div>
      {assets.map((asset) => (
        <div key={asset.id} className="border p-4 mb-2 rounded shadow">
          <h3 className="font-semibold">{asset.name}</h3>
          <p>Type: {asset.type ?? "N/A"}</p>
          <p>Status: {asset.status ?? "N/A"}</p>
          <p>Quantity: {asset.quantity ?? 0}</p>
          {asset.description && <p>Description: {asset.description}</p>}
        </div>
      ))}
    </div>
  );
};

export default AssetList;
