import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { useAppContext } from "@/context/AppContext";
import { Radio, Play, Square, Settings, ExternalLink } from "lucide-react";
import { toast } from "@/hooks/use-toast";

const AdminLivestream = () => {
  const { state, dispatch } = useAppContext();
  const [livestreamUrl, setLivestreamUrl] = useState(state.livestreamUrl || "");

  const handleToggleLivestream = (isLive: boolean) => {
    dispatch({
      type: 'SET_LIVESTREAM',
      payload: {
        isLive,
        url: isLive ? livestreamUrl : undefined
      }
    });

    toast({
      title: isLive ? "Livestream started" : "Livestream stopped",
      description: isLive 
        ? "Your church is now live streaming!" 
        : "The livestream has been stopped.",
    });
  };

  const handleUrlUpdate = () => {
    if (livestreamUrl) {
      dispatch({
        type: 'SET_LIVESTREAM',
        payload: {
          isLive: state.isLivestreaming,
          url: livestreamUrl
        }
      });

      toast({
        title: "Stream URL updated",
        description: "The livestream URL has been successfully updated.",
      });
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-bold text-foreground mb-2">Livestream Control</h2>
        <p className="text-muted-foreground">Manage your church's live broadcasting</p>
      </div>

      {/* Current Status */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center">
            <Radio className={`w-5 h-5 mr-2 ${state.isLivestreaming ? 'text-green-600' : 'text-gray-400'}`} />
            Current Status
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex items-center justify-between p-4 rounded-lg border">
            <div className="flex items-center space-x-3">
              <div className={`w-3 h-3 rounded-full ${
                state.isLivestreaming ? 'bg-green-500 animate-pulse' : 'bg-gray-400'
              }`} />
              <div>
                <p className="font-medium text-gray-300 dark:text-foreground">
                  {state.isLivestreaming ? 'Live Broadcasting' : 'Offline'}
                </p>
                <p className="text-sm text-muted-foreground">
                  {state.isLivestreaming ? 'Your service is currently live' : 'No active broadcast'}
                </p>
              </div>
            </div>
            {state.isLivestreaming && state.livestreamUrl && (
              <Button variant="outline" size="sm" asChild className={"text-gray-400"}>
                <a href={state.livestreamUrl} target="_blank" rel="noopener noreferrer">
                  <ExternalLink className="w-4 h-4 mr-2" />
                  View Stream
                </a>
              </Button>
            )}
          </div>
        </CardContent>
      </Card>

      {/* Stream Configuration */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center">
            <Settings className="w-5 h-5 mr-2" />
            Stream Configuration
          </CardTitle>
          <CardDescription>
            Configure your livestream settings and URLs
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="space-y-2">
            <Label className={"text-gray-400"} htmlFor="streamUrl" >Stream URL</Label>
            <div className="flex space-x-2">
              <Input
                id="streamUrl"
                type="url"
                value={livestreamUrl}
                onChange={(e) => setLivestreamUrl(e.target.value)}
                placeholder="https://www.youtube.com/watch?v=your-stream-id"
                className="flex-1 text-gray-800 dark:text-gray-200"
              />
              <Button onClick={handleUrlUpdate} className={"bg-gray-200"} variant="secondary">
                Update URL
              </Button>
            </div>
            <p className="text-sm text-muted-foreground">
              Enter your YouTube live stream URL, Facebook Live URL, or other streaming platform link
            </p>
          </div>

          <div className="flex items-center justify-between p-4 rounded-lg border">
            <div className="space-y-1">
              <Label htmlFor="live-toggle" className="text-gray-400 font-medium">
                Enable Livestream
              </Label>
              <p className="text-sm text-muted-foreground">
                Toggle your church's live broadcast on/off
              </p>
            </div>
            <Switch
              id="live-toggle"
              checked={state.isLivestreaming}
              onCheckedChange={handleToggleLivestream}
            />
          </div>
        </CardContent>
      </Card>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardContent className="p-6">
            <div className="flex items-center space-x-3 mb-4">
              <div className="w-10 h-10 bg-green-100 rounded flex items-center justify-center">
                <Play className="w-5 h-5 text-green-600" />
              </div>
              <div>
                <h3 className="font-semibold text-gray-300 dark:text-foreground">Start Broadcast</h3>
                <p className="text-sm text-muted-foreground">Begin live streaming</p>
              </div>
            </div>
            <Button 
              className="w-full bg-gray-200"
              variant={"secondary"}
              onClick={() => handleToggleLivestream(true)}
              disabled={state.isLivestreaming || !livestreamUrl}
            >
              {state.isLivestreaming ? 'Already Live' : 'Go Live'}
            </Button>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center space-x-3 mb-4">
              <div className="w-10 h-10 bg-red-100 rounded-lg flex items-center justify-center">
                <Square className="w-5 h-5 text-red-600" />
              </div>
              <div>
                <h3 className="font-semibold text-gray-300 dark:text-foreground">Stop Broadcast</h3>
                <p className="text-sm text-muted-foreground">End live streaming</p>
              </div>
            </div>
            <Button 
              variant="outline" 
              className="w-full text-gray-300"
              onClick={() => handleToggleLivestream(false)}
              disabled={!state.isLivestreaming}
            >
              {state.isLivestreaming ? 'Stop Stream' : 'Not Broadcasting'}
            </Button>
          </CardContent>
        </Card>
      </div>

      {/* Help Section */}
      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Livestream Setup Guide</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-3">
            <h4 className="font-semibold text-gray-300 dark:text-foreground">Getting Started</h4>
            <ol className="text-sm text-white dark:text-muted-foreground space-y-2 ml-4">
              <li>1. Set up your streaming software (OBS, XSplit, etc.)</li>
              <li>2. Configure your streaming platform (YouTube Live, Facebook Live)</li>
              <li>3. Copy the stream URL and paste it in the configuration above</li>
              <li>4. Test your stream before going live</li>
              <li>5. Toggle the livestream on when you're ready to broadcast</li>
            </ol>
          </div>

          <div className="space-y-3">
            <h4 className="font-semibold text-gray-300 dark:text-foreground">Supported Platforms</h4>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
              <div className="p-3 border rounded-lg">
                <h5 className="font-medium text-gray-300 dark:text-foreground">YouTube Live</h5>
                <p className="text-xs text-muted-foreground">Free streaming with chat</p>
              </div>
              <div className="p-3 border rounded-lg">
                <h5 className="font-medium text-gray-300 dark:text-foreground">Facebook Live</h5>
                <p className="text-xs text-muted-foreground">Social media integration</p>
              </div>
              <div className="p-3 border rounded-lg">
                <h5 className="font-medium text-gray-300 dark:text-foreground">Custom RTMP</h5>
                <p className="text-xs text-muted-foreground">Any streaming service</p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default AdminLivestream;