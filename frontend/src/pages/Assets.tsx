import React, { useEffect, useState } from 'react';
import { fetchAssets } from '../services/assetService';

interface Asset {
  id: number;
  name: string;
  type: string;
  status: string;
}

export default function Assets() {
  const [assets, setAssets] = useState<Asset[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchAssets()
      .then(data => setAssets(data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading assets...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Assets</h1>
      <ul>
        {assets.map(asset => (
          <li key={asset.id}>
            {asset.name} - {asset.type} - {asset.status}
          </li>
        ))}
      </ul>
    </div>
  );
}
