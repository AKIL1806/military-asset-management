import React, { useState } from 'react';

interface AssetFormProps {
  onSubmit: (data: { name: string; description: string }) => void;
}

const AssetForm: React.FC<AssetFormProps> = ({ onSubmit }) => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name) return alert('Name is required');
    onSubmit({ name, description });
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 p-4 border rounded">
      <div>
        <label className="block font-medium mb-1" htmlFor="name">Name</label>
        <input
          id="name"
          value={name}
          onChange={e => setName(e.target.value)}
          className="w-full border px-3 py-2 rounded"
          required
        />
      </div>
      <div>
        <label className="block font-medium mb-1" htmlFor="description">Description</label>
        <textarea
          id="description"
          value={description}
          onChange={e => setDescription(e.target.value)}
          className="w-full border px-3 py-2 rounded"
          rows={3}
        />
      </div>
      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Create Asset
      </button>
    </form>
  );
};

export default AssetForm;
