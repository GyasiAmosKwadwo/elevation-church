import { useEffect, useState } from "react";
import { Outlet, Link, useLocation, useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Sidebar, SidebarContent, SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";
import { useAppContext } from "@/context/AppContext";
import {Settings, Video, Book, Radio, Users, BarChart3, Calendar, Menu, LogOut} from "lucide-react";

const Admin = () => {
  const { state, dispatch } = useAppContext();
  const location = useLocation();
  const navigate = useNavigate();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  // Simulate admin login for demo
  useEffect(() => {
    if (!state.currentUser) {
      dispatch({
        type: 'SET_USER',
        payload: {
          id: '1',
          name: 'Admin User',
          role: 'admin'
        }
      });
    }
  }, [state.currentUser, dispatch]);

  const isActive = (path: string) => {
    return location.pathname === path || location.pathname.startsWith(path + '/');
  };

  const isAdminHome = location.pathname === '/admin';

  const AdminSidebar = () => (
    <div className=" space-y-2">
      <Link to="/admin/sermons">
        <Button
          variant={isActive('/admin/sermons') ? "default" : "ghost"}
          className={`w-full justify-start ${isActive('/admin/sermons') ?"dark:bg-gray-700 dark:hover:bg-gray-600" : "hover:bg-gray-200 rounded"}`}
        >
          <Video className="w-4 h-4 mr-2" />
          Sermons
        </Button>
      </Link>
      <Link to="/admin/series">
        <Button
          variant={isActive('/admin/series') ? "default" : "ghost"}
          className={`w-full justify-start ${isActive('/admin/series') ? "dark:bg-gray-700 dark:hover:bg-gray-600" : "hover:bg-gray-200 rounded"}`}
        >
          <Book className="w-4 h-4 mr-2" />
          Series
        </Button>
      </Link>
      <Link to="/admin/events">
        <Button
          variant={isActive('/admin/events') ? "default" : "ghost"}
          className={`w-full justify-start ${isActive('/admin/events') ? "dark:bg-gray-700 dark:hover:bg-gray-600" : "hover:bg-gray-200 rounded"}`}
        >
          <Calendar className="w-4 h-4 mr-2" />
          Events
        </Button>
      </Link>
      <Link to="/admin/livestream">
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
  );

  return (
    <div className="min-h-screen bg-mute dark:bg-slate-900">
      {/* Header */}
      {/*<header className="border-b bg-gray-950/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">*/}
      {/*  <div className="flex h-14 items-center justify-between px-4">*/}
      {/*    <Sheet open={sidebarOpen} onOpenChange={setSidebarOpen}>*/}
      {/*      <SheetTrigger asChild>*/}
      {/*        <Button variant="ghost" size="sm" className="md:hidden">*/}
      {/*          <Menu className="h-5 w-5" />*/}
      {/*        </Button>*/}
      {/*      </SheetTrigger>*/}
      {/*      <SheetContent side="left" className="w-64">*/}
      {/*        <div className="flex items-center mb-6">*/}
      {/*          <Settings className="w-6 h-6 mr-2" />*/}
      {/*          <h2 className="text-lg font-semibold">Admin Panel</h2>*/}
      {/*        </div>*/}
      {/*        <AdminSidebar />*/}
      {/*      </SheetContent>*/}
      {/*    </Sheet>*/}

      {/*    <p className={"hidden md:block text-gray-400 font-medium"}>*/}
      {/*      Hello Admin*/}
      {/*    </p>*/}
      

      {/*    <Button variant="outline" size="sm" onClick={() => navigate('/')}>*/}
      {/*      Back to Website*/}
      {/*    </Button>*/}
      {/*  </div>*/}
      {/*</header>*/}

      <div className="flex">
        {/* Desktop Sidebar */}
        <aside className="sticky top-[55px] bottom-0 h-[100vh] overflow-auto hidden  pb-2 md:flex w-64 flex-col border-r bg-gray-200/90 dark:bg-gray-950">
          <div >
            <div className="flex bg-gray-300/80 dark:bg-gray-800 items-center px-4 py-2 mb-2">
              <Settings className="w-6 h-6 mr-2 text-primary" />
              <h2 className="text-lg text-primary  font-semibold">Admin Panel</h2>
            </div>
            <div className="p-6 pt-0">
              <AdminSidebar />
            </div>
            
          </div>

          {/* Stats Card */}
          <div className="p-6 mt-auto">
            <Card className="dark:bg-gray-800">
              <CardHeader className="pb-2">
                <CardTitle className="text-sm text-gray-100 flex items-center">
                  <BarChart3 className="w-4 h-4 mr-2" />
                  Quick Stats
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-300 dark:text-muted-foreground">Sermons</span>
                  <span className="text-gray-400 font-medium">{state.sermons.length}</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-300 dark:text-muted-foreground">Series</span>
                  <span className="text-gray-400 font-medium">{state.series.length}</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-300 dark:text-muted-foreground">Events</span>
                  <span className="text-gray-400 font-medium">{state.events.length}</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-300 dark:text-muted-foreground">Status</span>
                  <span className={`text-xs font-medium ${
                    state.isLivestreaming ? 'text-green-600' : 'text-red-600'
                  }`}>
                    {state.isLivestreaming ? 'Live' : 'Offline'}
                  </span>
                </div>
              </CardContent>
            </Card>
          </div>

          <Link to="/admin">
            <Button
                variant={ "ghost"}
                className={`w-full justify-start hover:bg-gray-200 rounded`}
            >
              <LogOut className="w-4 h-4 mr-2" />
              Logut
            </Button>
          </Link>

        </aside>

        {/* Main Content */}
        <main className="flex-1 p-6">
          {isAdminHome ? (
            <div className="space-y-6 max-w-7xl">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <Link to="/admin/sermons">
                  <Card className="hover:shadow-md hover:bg-blue-900 dark:hover:bg-gray-700 transition-shadow cursor-pointer h-full">
                    <CardContent className="p-6 text-center">
                      <Video className="w-10 h-10 text-secondary dark:text-primary mx-auto mb-3" />
                      <h3 className="text-gray-300 font-semibold mb-1">Sermons</h3>
                      <p className="text-sm text-slate-400 text-muted-foreground">Manage sermons</p>
                      <p className="text-2xl font-bold text-secondary dark:text-primary mt-2">{state.sermons.length}</p>
                    </CardContent>
                  </Card>
                </Link>
                
                <Link to="/admin/series">
                  <Card className="hover:shadow-md hover:bg-blue-900 dark:hover:bg-gray-700 transition-shadow cursor-pointer h-full">
                    <CardContent className="p-6 text-center">
                      <Book className="w-10 h-10 text-secondary dark:text-primary mx-auto mb-3" />
                      <h3 className="text-gray-300 font-semibold mb-1">Series</h3>
                      <p className="text-slate-400 text-sm text-muted-foreground">Organize series</p>
                      <p className="text-2xl font-bold text-secondary dark:text-primary mt-2">{state.series.length}</p>
                    </CardContent>
                  </Card>
                </Link>

                <Link to="/admin/events">
                  <Card className="hover:shadow-md hover:bg-blue-900 dark:hover:bg-gray-700 transition-shadow cursor-pointer h-full">
                    <CardContent className="p-6 text-center">
                      <Calendar className="w-10 h-10 text-secondary dark:text-primary mx-auto mb-3" />
                      <h3 className="text-gray-300 font-semibold mb-1">Events</h3>
                      <p className="text-slate-400 text-sm text-muted-foreground">Manage events</p>
                      <p className="text-2xl font-bold text-secondary dark:text-primary mt-2">{state.events.length}</p>
                    </CardContent>
                  </Card>
                </Link>
                
                <Link to="/admin/livestream">
                  <Card className="hover:shadow-md hover:bg-blue-900 dark:hover:bg-gray-700 transition-shadow cursor-pointer h-full">
                    <CardContent className="p-6 text-center">
                      <Radio className="w-10 h-10 text-secondary dark:text-primary mx-auto mb-3" />
                      <h3 className="text-gray-300 font-semibold mb-1">Livestream</h3>
                      <p className="text-slate-400 text-sm text-muted-foreground">Control broadcast</p>
                      <div className={`text-sm font-medium mt-2 ${
                        state.isLivestreaming ? 'text-green-600' : 'text-red-600'
                      }`}>
                        {state.isLivestreaming ? '● LIVE' : '○ OFFLINE'}
                      </div>
                    </CardContent>
                  </Card>
                </Link>
              </div>

              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <Card>
                  <CardHeader>
                    <CardTitle className="text-gray-300">Recent Sermons</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-3">
                      {state.sermons.slice(0, 3).map((sermon) => (
                        <div key={sermon.id} className="flex items-center justify-between p-3 border rounded">
                          <div>
                            <h4 className="text-slate-300 font-medium text-sm">{sermon.title}</h4>
                            <p className="text-xs text-muted-foreground">
                              {new Date(sermon.date).toLocaleDateString()}
                            </p>
                          </div>
                          <Link to={`/sermons/${sermon.id}`}>
                            <Button variant="outline" className="rounded text-gray-100" size="sm">View</Button>
                          </Link>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>

                <Card>
                  <CardHeader>
                    <CardTitle className="text-gray-300">Upcoming Events</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-3">
                      {state.events.slice(0, 3).map((event) => (
                        <div key={event.id} className="flex items-center justify-between p-3 border rounded">
                          <div>
                            <h4 className="text-slate-300 font-medium text-sm">{event.title}</h4>
                            <p className="text-xs text-muted-foreground">
                              {new Date(event.date).toLocaleDateString()}
                            </p>
                          </div>
                          <Link to={`/events/${event.id}`}>
                            <Button variant="outline" className="rounded text-gray-100" size="sm">View</Button>
                          </Link>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              </div>
            </div>
          ) : (
            <Outlet />
          )}
        </main>
      </div>
    </div>
  );
};

export default Admin;