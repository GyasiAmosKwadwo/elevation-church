export function getYouTubeVideoId(url: string): string | null {
    const patterns = [
        /(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})/i,
        // Matches common YouTube URL patterns capturing 11-char ID
    ];

    for (const pattern of patterns) {
        const match = url.match(pattern);
        if (match && match[1]) {
            console.log(match[1])
            return match[1];
        }
    }

    return null; // No match found
}

// Example usage
// const urls = [
//     'https:
//     'https://youtu.be/dQw4w9WgXcQ',
// ];
//
// urls.forEach(url => {
//     const id = getYouTubeVideoId(url);
//     console.log(`URL: ${url}, ID: ${id}`);
// });
