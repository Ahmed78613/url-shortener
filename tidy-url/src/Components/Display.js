import React from 'react'

const Display = ({url}) => {
  return (
    <div>
      <h1>Enjoy your shortened Url</h1>
      <a href={url}>{url}</a>
    </div>
  )
}

export default Display
