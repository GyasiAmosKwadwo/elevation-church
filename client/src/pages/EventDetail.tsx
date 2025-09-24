import {useParams, Link, useNavigate} from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { useAppContext } from "@/context/AppContext";
import { Calendar, Clock, MapPin, ExternalLink, ArrowLeft } from "lucide-react";

const EventDetail = () => {
  const { id } = useParams();
  const { state } = useAppContext();
  const navigate = useNavigate();
  
  const event = state.events.find(e => e.id === id);

  if (!event) {
    return (
      <div className="container mx-auto px-4 py-12 text-center">
        <h1 className="text-3xl font-bold text-foreground mb-4">Event Not Found</h1>
        <p className="text-muted-foreground mb-8">The event you're looking for doesn't exist.</p>
        <Link to="/events">
          <Button variant={"secondary"}>Back to Events</Button>
        </Link>
      </div>
    );
  }

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

  return (
    <div className="container mx-auto px-6 py-8">
      {/* Back Button */}
      <Button variant="ghost" onClick={() => navigate('/events')} className="mb-4 mt-0">
        <ArrowLeft className="w-4 h-4 mr-2" />
        Back to Sermons
      </Button>

      <div className="grid grid-cols-1 lg:grid-cols-3 md:px-10 gap-8">
        <div className="lg:col-span-2">
          <div className="relative mb-6 rounded">
            <img 
              src={event.image} 
              alt={event.title}
              className="w-full h-64 md:h-80 object-cover rounded"
            />
            {event.featured && (
              <Badge className="absolute top-4 left-4 bg-primary text-primary-foreground">
                Featured Event
              </Badge>
            )}
          </div>

          <h1 className="text-3xl md:text-4xl font-bold text-blue-900 dark:text-foreground mb-4">
            {event.title}
          </h1>
          
          <p className="text-lg text-muted-foreground leading-relaxed">
            {event.description}
          </p>
        </div>

        <div className="lg:col-span-1">
          <Card className={"overflow-hidden"}>
            <CardHeader className={"p-0"}>
              <CardTitle className="bg-blue-500/20 dark:bg-gray-700 py-2 text-center text-lg" >Event Details</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4 mt-3">
              <div className="flex items-center">
                <Calendar className="w-5 h-5 mr-3 text-gray-400" />
                <div>
                  <p className="font-medium text-gray-50 dark:text-primary">{formatDate(event.date)}</p>
                </div>
              </div>
              
              <div className="flex items-center">
                <Clock className="w-5 h-5 mr-3 text-gray-400" />
                <div>
                  <p className="font-medium text-gray-50 dark:text-primary">{formatTime(event.time)}</p>
                </div>
              </div>
              
              <div className="flex items-start">
                <MapPin className="w-5 h-5 mr-3 text-gray-400 mt-0.5" />
                <div>
                  <p className="font-medium text-gray-50 dark:text-primary">{event.location}</p>
                </div>
              </div>

              {/*{event.registrationLink && (*/}
              {/*  <div className="pt-4">*/}
              {/*    <Button className="w-full text-gray-300 " variant={"secondary"} asChild>*/}
              {/*      <a href={event.registrationLink} target="_blank" rel="noopener noreferrer">*/}
              {/*        <ExternalLink className="w-4 h-4 mr-2" />*/}
              {/*        Register Now*/}
              {/*      </a>*/}
              {/*    </Button>*/}
              {/*  </div>*/}
              {/*)}*/}
            </CardContent>
          </Card>

          {/* Related Events */}
          <Card className="mt-6 overflow-hidden">
            <CardHeader className={"p-0"}>
              <CardTitle className="bg-blue-500/20 dark:bg-gray-700 py-2 text-center text-lg">Other Events</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3 mt-4">
                {state.events
                  .filter(e => e.id !== event.id)
                  .slice(0, 3)
                  .map((relatedEvent) => (
                    <Link 
                      key={relatedEvent.id} 
                      to={`/events/${relatedEvent.id}`}
                      className="block p-3 rounded border hover:bg-slate-900 transition-colors"
                    >
                      <h4 className="font-medium text-sm text-gray-300">{relatedEvent.title}</h4>
                      <p className="text-xs text-gray-400">
                        {formatDate(relatedEvent.date)}
                      </p>
                    </Link>
                  ))}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default EventDetail;