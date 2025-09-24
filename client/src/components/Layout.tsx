import { Outlet } from "react-router-dom";
import Header from "./Header";
import Footer from "./Footer";
import { useAppContext } from "@/context/AppContext";

const Layout = () => {
  const { state } = useAppContext();
  const isAdmin = state.currentUser?.role === 'admin';
  return (
    <div className="min-h-screen bg-gray-2000 bg-muted dark:bg-gray-900 flex flex-col">
      <Header />
      <main className="flex-1">
        <Outlet />
      </main>
      {!isAdmin && <Footer />}
    </div>
  );
};

export default Layout;