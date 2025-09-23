import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { FileUpload } from "@/components/ui/file-upload";
import { useAppContext } from "@/context/AppContext";
import { useToast } from "@/hooks/use-toast";
import { Settings } from "lucide-react";

const validationSchema = Yup.object({
  name: Yup.string().required('Church name is required').min(2, 'Name must be at least 2 characters'),
  logo: Yup.string().required('Church logo is required'),
});

const AdminSettings = () => {
  const { state, dispatch } = useAppContext();
  const { toast } = useToast();

  const formik = useFormik({
    initialValues: {
      name: state.churchSettings.name,
      logo: state.churchSettings.logo || '',
    },
    validationSchema,
    onSubmit: (values) => {
      dispatch({ type: 'UPDATE_CHURCH_SETTINGS', payload: values });
      toast({
        title: "Settings Updated",
        description: "Church settings have been successfully updated.",
      });
    },
  });

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-gray-50">Church Settings</h2>
        <p className="text-muted-foreground">Manage your church information and preferences</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="flex text-gray-100 items-center">
            <Settings className="w-5 h-5 mr-2" />
            General Settings
          </CardTitle>
          <CardDescription>
            Configure basic church information
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={formik.handleSubmit} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="name" className="text-slate-300">Church Name</Label>
              <Input
                id="name"
                name="name"
                value={formik.values.name}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                placeholder="Enter church name"
                className="text-gray-700 dark:text-gray-100"
              />
              {formik.touched.name && formik.errors.name && (
                <p className="text-sm text-red-400">{formik.errors.name}</p>
              )}
            </div>

            <div className="space-y-2">
              <Label htmlFor="logo" className="text-slate-300">Church Logo</Label>
              <FileUpload
                id="logo"
                name="logo"
                value={formik.values.logo}
                onChange={(value) => formik.setFieldValue('logo', value)}
                onBlur={formik.handleBlur}
                error={formik.touched.logo && formik.errors.logo ? formik.errors.logo : undefined}
              />
            </div>

            <div className="flex justify-start">
              <Button
                type="submit"
                variant="secondary"
                className="text-white disabled:cursor-not-allowed"
                disabled={!formik.isValid || !formik.dirty}
              >
                Save Changes
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default AdminSettings;