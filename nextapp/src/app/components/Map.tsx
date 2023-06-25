'use client'
import { GoogleMap, LoadScript } from "@react-google-maps/api";

const containerStyle = {
    width: '100%',
    height: '100%'  // Change this value based on your requirements
  };

  const center = {
    lat: -3.745,
    lng: -38.523
  };


export default function Map() {
    return (
        <LoadScript googleMapsApiKey="AIzaSyCymc4gO1jPLDwFB2zC_3WR6V20h_IgKzk">
          <GoogleMap
            mapContainerStyle={containerStyle}
            center={center}
            zoom={10}
          >
            {/* TODO: add markers here */}
          </GoogleMap>
        </LoadScript>
    )
}