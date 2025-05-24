import React from 'react';
import { useNavigate } from 'react-router-dom';
import AssetForm from '../components/AssetForm';
import { createAsset } from '../services/assetService';

const CreateAsset: React.FC = () => {
  const navigate = useNavigate();

  const handleCreate = async (data: { name: string; description: string }) => {
    try {
      await createAsset(data);
      alert('Asset created successfully!');
      navigate('/assets');  // Redirect to asset list page
    } catch (error) {
      alert('Error creating asset: ' + (error as Error).message);
    }
  };

  return (
    <div className="max-w-lg mx-auto mt-10">
      <h2 className="text-2xl font-bold mb-6">Create New Asset</h2>
      <AssetForm onSubmit={handleCreate} />
    </div>
  );
};

export default CreateAsset;
