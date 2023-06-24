'use client'

import { useState } from "react"
async function getData(address, search, type) {
    // console.log(address, search)
    // address, search, radius=500, place_type
    const res = await fetch('http://127.0.0.1:5000/search', {headers: {'Content-Type': 'application/json'}, method: 'POST', body: JSON.stringify({
        address: address,
        search: search,
        radius: 500,
        place_type: type,
    })})
   
    return res.json()
  }

export default function ({}) {
    const [ address, setAddress ] = useState('')
    const [search, setSearch] = useState('')
    const [placeType, setPlaceType] = useState('')
    const [result, setResult] = useState([])
    return (
        <>
        <input onChange={e => setAddress(e.target.value)}  onKeyDown={(e) => {
        }} type="text" name="address" id="address" className="shadow-lg block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Address"></input>
        <input onChange={e => setSearch(e.target.value)}  onKeyDown={(e) => {
        }} type="text" name="search" id="search" className="shadow-lg block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Search"></input>
       
        <input onChange={e => setPlaceType(e.target.value)}  onKeyDown={(e) => {
            if (e.key === 'Enter') {
                getData(address, search, placeType).then((data) => {
                    setResult(data)
                    console.log('data', data)
                })
            }
        }} type="text" name="place type" id="place_type" className="shadow-lg block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Place Type"></input>
        <div><ul>
            {result && result.map((r) => <li className='text-black'>{r}</li>)}
            </ul></div>
        </>
    )
}
