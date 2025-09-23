import { useState } from "react";
import {Link, useLocation, useNavigate} from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { useAppContext } from "@/context/AppContext";
import {Play, LogOut, Settings, Menu, X, Home, Book, BookMarked, Video, Calendar, Radio} from "lucide-react";
import ThemeToggle from "./ui/ThemeToggle";

const Header = () => {
  const location = useLocation();
  const { state } = useAppContext();
  const [isOpen, setIsOpen] = useState(false);
  
  const isActive = (path: string) => {
    return location.pathname === path || location.pathname.startsWith(path + '/');
  };

  const isAdmin = state.currentUser?.role === 'admin';

  if(isAdmin){
    return <AdminHeader />
  }

  return (
    <header className="bg-yellow-500 dark:bg-gray-950/95 backdrop-blur-sm border-b border-border sticky top-0 z-50">
      <div className="container mx-auto px-4">

        <div className="flex items-center justify-between h-16">
          {/* Mobile Navigation */}
          <div className="md:hidden flex items-center gap-2">
            <Sheet open={isOpen} onOpenChange={setIsOpen}>
              <SheetTrigger asChild>
                <Button variant="ghost" size="sm">
                  <Menu className="w-5 h-5" />
                </Button>
              </SheetTrigger>
              <SheetContent side="left" className="w-64">
                <div className="flex flex-col space-y-4 mt-8">
                  <Link 
                    to="/" 
                    onClick={() => setIsOpen(false)}
                    className={`flex items-center gap-2 text-sm font-medium transition-colors hover:text-primary ${
                      isActive('/') && location.pathname === '/' ? 'text-slate-400' : 'text-muted-foreground'
                    }`}
                  >
                    <Home />
                    Home
                  </Link>
                  <Link 
                    to="/sermons" 
                    onClick={() => setIsOpen(false)}
                    className={`flex items-center gap-2 text-sm font-medium transition-colors hover:text-primary ${
                      isActive('/sermons') ? 'text-slate-400' : 'text-muted-foreground'
                    }`}
                  >
                    <Book />
                    Sermons
                  </Link>
                  <Link 
                    to="/series" 
                    onClick={() => setIsOpen(false)}
                    className={`flex items-center gap-2 text-sm font-medium transition-colors hover:text-primary ${
                      isActive('/series') ? 'text-slate-400' : 'text-muted-foreground'
                    }`}
                  >
                    Series
                  </Link>
                  <Link 
                    to="/events" 
                    onClick={() => setIsOpen(false)}
                    className={`flex items-center gap-2 text-sm font-medium transition-colors hover:text-primary ${
                      isActive('/events') ? 'text-slate-400' : 'text-muted-foreground'
                    }`}
                  >
                    <BookMarked />
                    Events
                  </Link>
                </div>
              </SheetContent>
            </Sheet>

            <Link to="/" className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-primary rounded-full flex items-center justify-center">
                <img
                  src={state.churchSettings.logo}
                  alt="Church Logo"
                  className="w-8 h-8 rounded-full"
                />
              </div>
            </Link>
          </div>

          <Link to="/" className="hidden md:flex items-center space-x-2">
              <img
                src={state.churchSettings.logo}
                alt="Church Logo"
                className="w-8 h-8 rounded-full"
              />
            <span className="hidden md:block text-xl font-bold text-muted text-foreround">{state.churchSettings.name}</span>
          </Link>


          <nav className="hidden md:flex items-center space-x-6">
            <Link 
              to="/"
              className={`text-sm font-medium transition-colors hover:text-primary ${
                isActive('/') && location.pathname === '/' ? 'text-primary' : 'text-gray-100 dark:text-gray-400'
              }`}
            >
              Home
            </Link>
            <Link 
              to="/sermons" 
              className={`text-sm font-medium transition-colors hover:text-primary ${
                isActive('/sermons') ? 'text-primary' : 'text-gray-100 dark:text-gray-400'
              }`}
            >
              Sermons
            </Link>
            <Link 
              to="/series" 
              className={`text-sm font-medium transition-colors hover:text-primary ${
                isActive('/series') ? 'text-primary' : 'text-gray-100 dark:text-gray-400'
              }`}
            >
              Series
            </Link>
            <Link 
              to="/events" 
              className={`text-sm font-medium transition-colors hover:text-primary ${
                isActive('/events') ? 'text-primary' : 'text-gray-100 dark:text-gray-400'
              }`}
            >
              Events
            </Link>
          </nav>


          <div className="flex items-center space-x-4">
            <ThemeToggle />
            {state.isLivestreaming && (
              <Button variant="secondary" size="sm" asChild className="rounded text-yellow-300 dark:text-white bg-blue-900 dark:bg-gray-700">
                <Link to="#livestream">
                  <Play className="w-4 h-4 mr-2" />
                  Live Now
                </Link>
              </Button>
            )}
            
            {isAdmin && (
              <Button variant="outline" size="sm" asChild className="rounded text-gray-300">
                <Link to="/admin">
                  <Settings className="w-4 h-4 mr-2" />
                  Admin
                </Link>
              </Button>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;


const AdminHeader =()=>{
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const navigate = useNavigate();

  const isActive = (path: string) => {
    return location.pathname === path || location.pathname.startsWith(path + '/');
  };
  return(
      <>
        {/* Header */}
        <header className="sticky top-0 z-50 border-b bg-yellow-500/95 dark:bg-gray-950/95 backdrop-blur ">
          <div className="flex h-14 items-center justify-between px-4">
            <Sheet open={sidebarOpen} onOpenChange={setSidebarOpen}>
              <SheetTrigger asChild>
                <Button variant="ghost" size="sm" className="md:hidden">
                  <Menu className="h-5 w-5" />
                </Button>
              </SheetTrigger>
              <SheetContent side="left" className="w-64 bg-gray-100 dark:bg-gray-800">
                <div className="flex items-center mb-6">
                  <Settings className="w-6 h-6 mr-2 text-blue-900 dark:tex-white" />
                  <h2 className="text-lg text-blue-900 dark:text-white font-semibold">Admin Panel</h2>
                </div>
                <AdminSidebar isActive={isActive} isOpen={setSidebarOpen} />
              </SheetContent>
            </Sheet>

            <p className={"hidden md:block text-blue-900 dark:text-gray-200 font-medium"}>
              Hello Admin
            </p>


            <div className={"flex gap-2"}>
              <ThemeToggle />

              <Button variant="outline" size="sm" onClick={() => navigate('/')}>
                Go to Website
              </Button>
            </div>

          </div>
        </header>
      </>
  )
}

const AdminSidebar = ({isActive , isOpen} : {isActive : (path : string)=> void ; isOpen: (state: boolean)=> void}) => (
    <div className="flex flex-col h-[100vh] overflow-auto">
      <div className={"flex-1 space-y-2"}>
        <Link
            to="/admin/sermons"
            // onClick={()=> isOpen(false)}
        >
          <Button
              variant={isActive('/admin/sermons') ? "default" : "ghost"}
              onClick={()=> isOpen(false)}
              className={`w-full justify-start ${isActive('/admin/sermons') ? "dark:bg-gray-700 dark:hover:bg-gray-600" : "hover:bg-gray-200 rounded"}`}
          >
            <Video className="w-4 h-4 mr-2" />
            Sermons
          </Button>
        </Link>
        <Link
            to="/admin/series"
            onClick={()=> isOpen(false)}
        >
          <Button
              variant={isActive('/admin/series') ? "default" : "ghost"}
              className={`w-full justify-start ${isActive('/admin/series') ? "dark:bg-gray-700 dark:hover:bg-gray-600" : "hover:bg-gray-200 rounded"}`}
          >
            <Book className="w-4 h-4 mr-2" />
            Series
          </Button>
        </Link>
        <Link
            to="/admin/events"
            onClick={()=> isOpen(false)}
        >
          <Button
              variant={isActive('/admin/events') ? "default" : "ghost"}
              className={`w-full justify-start ${isActive('/admin/events') ? "dark:bg-gray-700 dark:hover:bg-gray-600": "hover:bg-gray-200 rounded"}`}
          >
            <Calendar className="w-4 h-4 mr-2" />
            Events
          </Button>
        </Link>
        <Link
            to="/admin/livestream"
            onClick={()=> isOpen(false)}
        >
          <Button
              variant={isActive('/admin/livestream') ? "default" : "ghost"}
              className={`w-full justify-start ${isActive('/admin/livestream') ? "dark:bg-gray-700 dark:hover:bg-gray-600" : "hover:bg-gray-200 rounded"}`}
          >
            <Radio className="w-4 h-4 mr-2" />
            Livestream
          </Button>
        </Link>
        <Link to="/admin/settings">
          <Button
              variant={isActive('/admin/settings') ? "default" : "ghost"}
              className={`w-full justify-start ${isActive('/admin/settings') ? "dark:bg-gray-700 dark:hover:bg-gray-600" : "hover:bg-gray-200 rounded"}`}
          >
            <Settings className="w-4 h-4 mr-2" />
            Settings
          </Button>
        </Link>
      </div>

      <div className={"mb-20"}>
        <Link to="/admin">
          <Button
              variant={ "ghost"}
              className={`self-end w-full justify-start hover:bg-gray-200`}
              onClick={()=> isOpen(false)}
          >
            <LogOut className="w-4 h-4 mr-2" />
            Logut
          </Button>
        </Link>
      </div>

    </div>
);