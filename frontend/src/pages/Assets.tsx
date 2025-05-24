import React, { useEffect, useState } from 'react';
import { fetchAssets } from '../services/assetService';

interface Asset {
  id: number;
  name: string;
  type: string;
  status: string;
}

const Assets: React.FC = () => {
  const [assets, setAssets] = useState<Asset[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchAssets()
      .then((data: Asset[]) => setAssets(data))
      .catch((err: Error) => setError(err.message || 'Unknown error'))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p className="text-center mt-10">Loading assets...</p>;
  if (error) return <p className="text-center mt-10 text-red-600">Error: {error}</p>;

  return (
    <section className="max-w-4xl mx-auto mt-10 px-4">
      <h1 className="text-3xl font-bold mb-6">Assets</h1>
      {assets.length === 0 ? (
        <p>No assets found.</p>
      ) : (
        <ul className="space-y-4">
          {assets.map(asset => (
            <li
              key={asset.id}
              className="p-4 border rounded shadow-sm hover:shadow-md transition-shadow"
            >
              <p><strong>Name:</strong> {asset.name}</p>
              <p><strong>Type:</strong> {asset.type}</p>
              <p><strong>Status:</strong> {asset.status}</p>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
};

export default Assets;
