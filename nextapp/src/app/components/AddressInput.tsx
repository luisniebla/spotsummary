'use client'

import { useState } from "react"
async function getData(address) {
    // address, search, radius=500, place_type
    const res = await fetch('http://127.0.0.1:5000/search', {headers: {'Content-Type': 'application/json'}, method: 'POST', body: JSON.stringify({
        address: '15125 N Scottsdale Rd',
        search: 'coffee',
        radius: 500,
        place_type: 'cafe'
    })})
   
    return res.json()
  }

export default function ({}) {
    const [ address, setAddress ] = useState('')
    const [result, setResult] = useState([])
    return (
        <>
        <input onChange={e => setAddress(e.target.value)}  onKeyDown={(e) => {
            if (e.key === 'Enter') {
                getData(address).then((data) => {
                    setResult(data)
                    console.log('data', data)
                })
            }
        }} type="text" name="price" id="price" className="shadow-lg block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Address"></input>
        <div><ul>
            {result && result.map((r) => <li className='text-black'>{r}</li>)}
            </ul></div>
        </>
    )
}
