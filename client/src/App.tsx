import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AppProvider } from "@/context/AppContext";
import Layout from "@/components/Layout";
import ScrollToTop from "@/components/ScrollToTop";
import Home from "@/pages/Home";
import Sermons from "@/pages/Sermons";
import SermonDetail from "@/pages/SermonDetail";
import Series from "@/pages/Series";
import SeriesDetail from "@/pages/SeriesDetail";
import Events from "@/pages/Events";
import EventDetail from "@/pages/EventDetail";
import Admin from "@/pages/Admin";
import AdminSermons from "@/pages/admin/AdminSermons";
import AdminSeries from "@/pages/admin/AdminSeries";
import AdminEvents from "@/pages/admin/AdminEvents";
import AdminSettings from "@/pages/admin/AdminSettings";
import AdminLivestream from "@/pages/admin/AdminLivestream";
import NotFound from "./pages/NotFound";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <AppProvider>
      <TooltipProvider>
        <Toaster />
        <Sonner />
        <BrowserRouter>
          <ScrollToTop />
          <Routes>
            <Route path="/" element={<Layout />}>
              <Route index element={<Home />} />
              <Route path="sermons" element={<Sermons />} />
              <Route path="sermons/:id" element={<SermonDetail />} />
              <Route path="series" element={<Series />} />
              <Route path="series/:id" element={<SeriesDetail />} />
              <Route path="events" element={<Events />} />
              <Route path="events/:id" element={<EventDetail />} />
              <Route path="admin" element={<Admin />}>
                <Route index element={<AdminSermons />} />
                <Route path="sermons" element={<AdminSermons />} />
                <Route path="series" element={<AdminSeries />} />
                <Route path="events" element={<AdminEvents />} />
                <Route path="settings" element={<AdminSettings />} />
                <Route path="livestream" element={<AdminLivestream />} />
              </Route>
            </Route>
            <Route path="*" element={<NotFound />} />
          </Routes>
        </BrowserRouter>
      </TooltipProvider>
    </AppProvider>
  </QueryClientProvider>
);

export default App;
