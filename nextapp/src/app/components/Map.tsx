'use client'
import { GoogleMap, LoadScript, Marker } from "@react-google-maps/api";
// import { loadEnvConfig } from '@next/env'
import { useState } from 'react'
// loadEnvConfig(process.cwd())

const containerStyle = {
    width: '100%',
    height: '100%'  // Change this value based on your requirements
  };

  const center = {
    lat: 33.448376,
    lng: -38.523
  };



export default function Map() {
  console.log(process.env.NEXT_PUBLIC_MAPS_API_KEY)
  // console.log(process.env.MAPS_API_KEY)
  navigator.geolocation.getCurrentPosition(function(location) {
    setCoords(location.coords)
  });
  const [coords, setCoords] = useState({})
    return (
        <LoadScript googleMapsApiKey={process.env.NEXT_PUBLIC_MAPS_API_KEY}>
          <GoogleMap
            mapContainerStyle={containerStyle}
            center={{
              lat: coords.latitude,
              lng: coords.longitude,
            }}
            zoom={10}
          >
            {/* TODO: add markers here */}
          </GoogleMap>
        </LoadScript>
    )
}