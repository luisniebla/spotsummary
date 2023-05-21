import React, { useState, useDeferredValue, Suspense, useEffect } from 'react';
import axios

const SearchResults = ({search}) => {
    return <>

    </>
}

const AsyncComponent = () => {


    const [loading, setLoading] = useState(true);
    const [data, setData] = useState(null);


    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await axios.get(
            "http://universities.hipolabs.com/search?country=United+States"
          );
          setData(response.data);
          setLoading(false);
        } catch (e) {
          setLoading(false);
          setData([]);
        }
      };
      fetchData();
    });
    return (
      <>
        {loading ? (
          <p>Loading please wait...</p>
        ) : (
          <ul>
            {data.map((item) => (
                <li>{item.name}</li>
            ))}
          </ul>
        )}
      </>
    );
   };

export default function Test() {
    const [search, setSearch] = useState('')
    const deferredSearch = useDeferredValue(search)

    return <>
        <input value={search} onChange= {e => setSearch(e.target.value)} />
        <p>Search: {deferredSearch}</p>
        <Suspense fallback={<p>Loading, please wait...</p>}>
       <AsyncSuspendableComponent />
     </Suspense>
    </>
}