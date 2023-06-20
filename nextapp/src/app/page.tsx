
import Image from 'next/image'


async function getData() {
  const res = await fetch('http://127.0.0.1:5000/search', {method: 'POST'})
  // The return value is *not* serialized
  // You can return Date, Map, Set, etc.
 
  // Recommendation: handle errors
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error('Failed to fetch data')
  }
 
  return res.json()
}

export default async function Home() {
  // const data = await getData()
  return (
    <body>
      
      <div className="flex h-screen border-black border-l">
        <div className="w-1/3 bg-white p-4">
          <h1 className="text-4xl mb-4 text-black">Find a Spot</h1>
          <input  type="text" name="price" id="price" className="shadow-lg block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Address"></input>
        </div>
        <div className="w-1/2">
          <div>Hello</div>
          {/* <Map 
            google={props.google}
            style={style}
          /> */}
        </div>
      </div>
    </body>
  )
}
