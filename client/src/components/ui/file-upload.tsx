import { useState, useRef } from 'react';
import { Button } from './button';
import { Input } from './input';
import { Label } from './label';
import { Upload, X } from 'lucide-react';
import { cn } from '@/lib/utils';

interface FileUploadProps {
  id?: string;
  name: string;
  value: string;
  onChange: (value: string) => void;
  onBlur?: () => void;
  accept?: string;
  className?: string;
  label?: string;
  error?: string;
}

export const FileUpload = ({ 
  id, 
  name, 
  value, 
  onChange, 
  onBlur,
  accept = "image/*",
  className,
  label,
  error
}: FileUploadProps) => {
  const [preview, setPreview] = useState<string>(value);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const result = e.target?.result as string;
        setPreview(result);
        onChange(result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleRemove = () => {
    setPreview('');
    onChange('');
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleClick = () => {
    fileInputRef.current?.click();
  };

  return (
    <div className={cn("space-y-2 ", className)}>
      {label && <Label htmlFor={id}>{label}</Label>}
      
      <div className="space-y-2">
        {/* File input */}
        <input
          ref={fileInputRef}
          id={id}
          name={name}
          type="file"
          accept={accept}
          onChange={handleFileChange}
          onBlur={onBlur}
          className="hidden"
        />
        
        {/* Upload button */}
        {!preview && (
          <Button
            type="button"
            variant="outline"
            onClick={handleClick}
            className="hover:bg-gray-200 dark:hover:bg-gray-700 w-full h-32 border-blue-900 border-dashed"
          >
            <div className="flex flex-col items-center">
              <Upload className="w-6 h-6 mb-2 text-muted-foreground" />
              <span className="text-sm text-muted-foreground">Click to upload image</span>
            </div>
          </Button>
        )}
        
        {/* Preview */}
        {preview && (
          <div className="relative">
            <img
              src={preview}
              alt="Preview"
              className="w-full h-40 object-contain rounded-lg border"
            />
            <Button
              type="button"
              variant="destructive"
              size="sm"
              onClick={handleRemove}
              className="absolute top-2 right-2"
            >
              <X className="w-4 h-4" />
            </Button>
          </div>
        )}
        
        {/* URL input fallback */}
        {/* <div className="flex gap-2">
          <Input
            placeholder="Or paste image URL"
            value={value && !preview ? value : ''}
            onChange={(e) => {
              onChange(e.target.value);
              setPreview(e.target.value);
            }}
            onBlur={onBlur}
          />
        </div> */}
      </div>
      
      {error && <p className="text-sm text-red-400">{error}</p>}
    </div>
  );
};