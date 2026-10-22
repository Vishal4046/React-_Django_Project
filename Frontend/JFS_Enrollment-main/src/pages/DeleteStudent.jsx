
import React, { useEffect } from 'react'
import axios from 'axios'
import { useNavigate, useParams } from 'react-router-dom'

const DeleteStudent = () => {
  const { id } = useParams()
  const navigate = useNavigate()

  useEffect(() => {
    axios.delete(`http://localhost:3000/users/${id}`)
      .then(() => {
        alert("Student deleted successfully")
        navigate('/viewstudent')
      })
      .catch(err => {
        console.log(err)
        alert("Failed to delete student")
        navigate('/viewstudent')
      })
  }, [id, navigate])

  return (
    <div>
      <h2>Deleting Student...</h2>
    </div>
  )
}

export default DeleteStudent
