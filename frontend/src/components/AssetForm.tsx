import React, { useState } from "react";
import type { Asset } from "../services/assetService";

interface AssetFormProps {
  onAdd: (asset: Asset) => void;
}

const AssetForm: React.FC<AssetFormProps> = ({ onAdd }) => {
  const [name, setName] = useState("");
  const [type, setType] = useState("");
  const [status, setStatus] = useState("active");
  const [quantity, setQuantity] = useState(1);
  const [baseId, setBaseId] = useState(1);
  const [description, setDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (!name.trim()) {
      setError("Name is required");
      return;
    }
    if (!type.trim()) {
      setError("Type is required");
      return;
    }
    if (!status.trim()) {
      setError("Status is required");
      return;
    }
    if (quantity < 1) {
      setError("Quantity must be at least 1");
      return;
    }
    if (baseId < 1) {
      setError("Base ID must be at least 1");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/api/v1/assets", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          type,
          status,
          quantity,
          base_id: baseId,
          description,
        }),
      });

      if (!response.ok) {
        throw new Error(`Failed to create asset: ${response.statusText}`);
      }

      const newAsset: Asset = await response.json();
      onAdd(newAsset);

      setName("");
      setType("");
      setStatus("active");
      setQuantity(1);
      setBaseId(1);
      setDescription("");
    } catch (err) {
      setError("Failed to create asset");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md p-4 border rounded shadow-sm">
      <h2 className="text-lg font-semibold mb-4">Add New Asset</h2>

      {error && <p className="text-red-600 mb-2">{error}</p>}

      <label className="block mb-2">
        Name <span className="text-red-500">*</span>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="mt-1 block w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500"
          disabled={loading}
          required
        />
      </label>

      <label className="block mb-2">
        Type <span className="text-red-500">*</span>
        <input
          type="text"
          value={type}
          onChange={(e) => setType(e.target.value)}
          className="mt-1 block w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500"
          disabled={loading}
          required
        />
      </label>

      <label className="block mb-2">
        Status <span className="text-red-500">*</span>
        <input
          type="text"
          value={status}
          onChange={(e) => setStatus(e.target.value)}
          className="mt-1 block w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500"
          disabled={loading}
          required
        />
      </label>

      <label className="block mb-2">
        Quantity <span className="text-red-500">*</span>
        <input
          type="number"
          min={1}
          value={quantity}
          onChange={(e) => setQuantity(Number(e.target.value))}
          className="mt-1 block w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500"
          disabled={loading}
          required
        />
      </label>

      <label className="block mb-2">
        Base ID <span className="text-red-500">*</span>
        <input
          type="number"
          min={1}
          value={baseId}
          onChange={(e) => setBaseId(Number(e.target.value))}
          className="mt-1 block w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500"
          disabled={loading}
          required
        />
      </label>

      <label className="block mb-4">
        Description
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="mt-1 block w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500"
          disabled={loading}
          rows={3}
        />
      </label>

      <button
        type="submit"
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? "Adding..." : "Add Asset"}
      </button>
    </form>
  );
};

export default AssetForm;
