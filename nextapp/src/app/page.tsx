
// import 'dotenv/config'
import Image from 'next/image'
import Search from './components/Search'
import Map from './components/Map'


export default async function Home() {
  // const data = await getData()
  // console.log(process.env.REACT_APP_API_KEY)
  console.log('NEXT_PUBLIC_KEY', process.env.NEXT_PUBLIC_KEY)
  return (
    <body>

      <div className="flex h-screen border-black border-l">
        <div className="w-1/3 bg-white p-4">
          <h1 className="text-4xl mb-4 text-black">Find a Spot</h1>
          <Search />
        </div>
        <div className="w-2/3">
          <Map/>

          {/* <iframe
            width="100%"
            height="450"
            style={{border: 0}}
            loading="lazy"
            allowfullscreen
            referrerpolicy="no-referrer-when-downgrade"
            src="https://www.google.com/maps/embed/v1/place?key=AIzaSyCymc4gO1jPLDwFB2zC_3WR6V20h_IgKzk
              &q=Space+Needle,Seattle+WA"> */}
          {/* </iframe> */}
        </div>
      </div>
    </body>
  )
}
