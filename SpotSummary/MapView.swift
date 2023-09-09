import SwiftUI
import MapKit

struct MapView: UIViewRepresentable {

    func makeAnnotation() -> MKPointAnnotation {
        let cafeCoordinate = CLLocationCoordinate2D(latitude: 37.7749, longitude: -122.4194) // Example coordinate
        let annotation = MKPointAnnotation()
        annotation.coordinate = cafeCoordinate
        annotation.title = "Best Cafe in Town"
        annotation.subtitle = "Try the espresso!"
        return annotation
    }

    func makeUIView(context: Context) -> MKMapView {
        let mapView = MKMapView()
        let annotation = makeAnnotation()
        mapView.addAnnotation(annotation)
        
        let region = MKCoordinateRegion(center: annotation.coordinate, span: MKCoordinateSpan(latitudeDelta: 0.05, longitudeDelta: 0.05))
        mapView.setRegion(region, animated: true)
        
        return mapView
    }

    func updateUIView(_ uiView: MKMapView, context: Context) {
        // Update logic if needed
    }
}

struct ContentView: View {
    var body: some View {
        VStack {
            MapView()   // Embed the MapView here
                .frame(height: 1000)  // Set the desired frame
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
