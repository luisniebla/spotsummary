'use client'

import { useState } from "react"
import { Form, Field } from 'react-final-form'

function onSubmit(setResult) {
    return async function(values) {
    // console.log(address, search)
    // address, search, radius=500, place_type
    console.log(values)
    setResult([])
    const res = await fetch('http://127.0.0.1:5000/search', {headers: {'Content-Type': 'application/json'}, method: 'POST', body: JSON.stringify(values)})


    setResult(await res.json())
  }
}

const fancyInput = 'shadow-lg block w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 text-black placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'
export default function Search({}) {
    const [result, setResult] = useState([])
    console.log(result)
    return (
        <Form
        onSubmit={onSubmit(setResult)}
        render={({ handleSubmit, submitting }) => (
            <>
            <form onSubmit={handleSubmit} sadvadv={console.log(submitting)}>
                <label htmlFor="Address">Address</label>
                <Field
                    type="text"
                    id="address"
                    name="address"
                    required
                    className={fancyInput}
                    component="input"
                    onBlur={() => console.log('blur')}
                />
                <label htmlFor="search">Search:</label>
                <Field type="text" id="search" name="search" required component='input' className={fancyInput}/>
                <label htmlFor="radius">Radius:</label>
                <Field type="text" id="radius" name="radius" required component='input' className={fancyInput}/>
                <label htmlFor="place_type">Place Type:</label>
                <Field type="text" id="place_type" name="place_type" required component='input' className={fancyInput} />
                <button className='mt-3 px-4 py-2 bg-pink-500 text-white rounded-full hover:bg-pink-600 focus:outline-none focus:ring-2 focus:ring-pink-400 focus:ring-opacity-50' type="submit">Submit</button>
            </form>

            <ul>
            {result && result.map((r) => <li key={r} className='text-black'>{r}</li>)}
            </ul>
            </>
        )}/>
    )
}
