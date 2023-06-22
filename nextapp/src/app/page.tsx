
import Image from 'next/image'
import AddressInput from './components/AddressInput'



export default async function Home() {
  // const data = await getData()
  return (
    <body>
      
      <div className="flex h-screen border-black border-l">
        <div className="w-1/3 bg-white p-4">
          <h1 className="text-4xl mb-4 text-black">Find a Spot</h1>
          <AddressInput />
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
