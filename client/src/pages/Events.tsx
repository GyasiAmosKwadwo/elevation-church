import {Link, useNavigate} from "react-router-dom";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { useAppContext } from "@/context/AppContext";
import {Calendar, Clock, MapPin, ExternalLink, Search} from "lucide-react";
import {videos} from "@/assets/assets";
import {useState} from "react";
import {Input} from "@/components/ui/input";

const Events = () => {
  const { state } = useAppContext();
  const [searchTerm, setSearchTerm] = useState("");
  const navigate = useNavigate();


  const formatDate = (dateStr: string) => {
    return new Date(dateStr).toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };

  const formatTime = (timeStr: string) => {
    return new Date(`2000-01-01T${timeStr}`).toLocaleTimeString('en-US', {
      hour: 'numeric',
      minute: '2-digit',
      hour12: true
    });
  };

  const SearchEvent = state.events.filter((series) => {
    const matchesSearch = series.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        series.description.toLowerCase().includes(searchTerm.toLowerCase())


    return matchesSearch;
  });

  return (
    <div className="">
      {/* Hero Section */}
      <section className="relative h-[390px] overflow-hidden">
        {/* Background Video */}
        <video
            autoPlay
            muted
            loop
            className="absolute inset-0 w-full h-full object-cover"
        >
          <source src={videos.video_02} type="video/mp4" />
        </video>

        {/* Overlay */}
        <div className="absolute inset-0 bg-black/70" />

        <div className="relative h-full flex flex-col items-center justify-center  px-5 z-20 text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold text-white dark:text-foreground mb-4">
            Upcoming Events
          </h1>
          <p className="text-lg text-white dark:text-muted-foreground max-w-2xl mx-auto">
            Join us for these special gatherings as we grow together in faith and fellowship.
          </p>

          <div className={"w-full"}>
            <div className="relative max-w-lg md mx-auto mt-9">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground w-4 h-4" />
              <Input
                  placeholder="Search sermons, topics, or preachers..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="pl-10 "
              />
            </div>
          </div>
        </div>



      </section>


      {/* Events Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 py-8 px-4 md:px-14 lg:px-17">
        {state.events.map((event) => (
          <Card key={event.id} className="overflow-hidden hover:shadow-lg transition-shadow">
            <div
                className="cursor-pointer relative"
                onClick={()=> navigate(`/events/${event.id}`)}
            >
              <img
                src={event.image} 
                alt={event.title}
                className="w-full h-48 object-cover rounded-t-lg"
              />
              {event.featured && (
                <Badge className="absolute top-4 left-4 bg-gray-700 text-primary-foreground">
                  Featured
                </Badge>
              )}
            </div>
            
            <CardHeader
                className={""}
            >
              <CardTitle className="text-xl">{event.title}</CardTitle>
            </CardHeader>
            
            <CardContent className="space-y-4">
              <p className="text-gray-300">{event.description}</p>
              
              <div className="space-y-2">
                <div className="flex items-center text-sm text-slate-300 dark:text-muted-foreground">
                  <Calendar className="w-4 h-4 mr-2" />
                  {formatDate(event.date)}
                </div>
                <div className="flex items-center text-sm text-slate-300 dark:text-muted-foreground">
                  <Clock className="w-4 h-4 mr-2" />
                  {formatTime(event.time)}
                </div>
                <div className="flex items-center text-sm text-slate-300 dark:text-muted-foreground">
                  <MapPin className="w-4 h-4 mr-2" />
                  {event.location}
                </div>
              </div>

              <div className="flex items-center gap-2 pt-4">
                <Link to={`/events/${event.id}`} className="flex-1">
                  <Button variant={"secondary"} className="w-full bg-gray-100 hover:bg-gray-200">Learn More</Button>
                </Link>
                {event.registrationLink && (
                  <Button variant="outline" size="sm" asChild className={"text-gray-300"}>
                    <a href={event.registrationLink} target="_blank" rel="noopener noreferrer">
                      <ExternalLink className="w-4 h-4 " />
                    </a>
                  </Button>
                )}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default Events;