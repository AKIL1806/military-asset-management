import React from "react";
import type { Asset } from "../services/assetService";

interface AssetListProps {
  assets: Asset[];
}

const AssetList: React.FC<AssetListProps> = ({ assets }) => {
  return (
    <div>
      {assets.length === 0 ? (
        <p>No assets found.</p>
      ) : (
        assets.map((asset) => (
          <div key={asset.id} className="border p-4 mb-2 rounded shadow">
            <h3 className="font-semibold">{asset.name}</h3>
            <p>Type: {asset.type}</p>
            <p>Status: {asset.status}</p>
            <p>Quantity: {asset.quantity}</p>
            {asset.description && <p>Description: {asset.description}</p>}
          </div>
        ))
      )}
    </div>
  );
};

export default AssetList;
