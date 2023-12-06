import React, { FormEvent, useEffect, useRef, useState } from "react";
import axios from "axios";
import Courselist from "../pages/Courselist";
import { useAppSelector } from "../redux/hooks";
import { selectUser } from "../redux/slices/authSlice";
import "../styles/class.scss";
import "../styles/course-list-popup.scss";

interface Class {
  classId: number;
  className: string;
  classDescription: string;
  course: string;
  image: string;
  teacher_name: string;
  students: string[];
  classCode: string;
}

interface ClassModalProps {
  closeModal: () => void;
  classes: Class[];
  setClasses: (classes: Class[]) => void;
}

interface Course {
  course_id: string;
  syllabus: number;
  course_title: string;
  short_description: string;
  long_description: string;
  image: string;
}

function ClassModal({ closeModal, classes, setClasses }: ClassModalProps) {
  const user = useAppSelector(selectUser);
  const nameRef = useRef<HTMLInputElement>(null);
  const descriptionRef = useRef<HTMLTextAreaElement>(null);
  const [courseValue, setCourseValue] = useState("");
  const [selectedCourseTitle, setSelectedCourseTitle] = useState("");
  const [courses, setCourses] = useState<Course[]>([]);
  const [showCourselist, setShowCourselist] = useState(false);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/course/details/"
        );
        setCourses(response.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchCourses();
  }, []);

  const toggleCourseList = () => {
    setShowCourselist(!showCourselist);
  };

  const handleCourseSelect = (
    selectedCourseId: string,
    selectedTitle: string
  ) => {
    setCourseValue(selectedCourseId);
    setSelectedCourseTitle(selectedTitle);
    setShowCourselist(false);
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const name = nameRef.current?.value;
    const description = descriptionRef.current?.value;

    try {
      if (user.token.type === "T") {
        if (!name || !description) {
          console.error("Required fields are missing");
          return;
        }
        const response = await axios.post("http://127.0.0.1:8000/classes/", {
          className: name,
          classDescription: description,
          course: courseValue,
          teacher: user.token.id,
          students: ["stud"],
        });

        if (response.status === 201) {
          closeModal();
          setClasses([...classes, response.data]);
        }
      } else {
        if (!name) {
          console.error("Required fields are missing");
          return;
        }
        const response = await axios.post(
          "http://127.0.0.1:8000/join-requests/",
          {
            class_code: name,
            student: user.token.id,
          }
        );
        if (response.status === 201) {
          closeModal();
        }
      }
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div id="modal" className="modal">
      <div className="modal-content">
        <div className="modal-header">
          <h1>{user.token.type === "T" ? "Create Class" : "Join Class"}</h1>
          <span className="close" onClick={closeModal}>
            &times;
          </span>
        </div>
        {showCourselist ? (
          <div className="course-list-popup">
            <button className="button">
              <div className="button-box">
                <span className="button-elem">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 46 40">
                    <path d="M46 20.038c0-.7-.3-1.5-.8-2.1l-16-17c-1.1-1-3.2-1.4-4.4-.3-1.2 1.1-1.2 3.3 0 4.4l11.3 11.9H3c-1.7 0-3 1.3-3 3s1.3 3 3 3h33.1l-11.3 11.9c-1 1-1.2 3.3 0 4.4 1.2 1.1 3.3.8 4.4-.3l16-17c.5-.5.8-1.1.8-1.9z"></path>
                  </svg>
                </span>
                <span className="button-elem">
                  <svg viewBox="0 0 46 40">
                    <path d="M46 20.038c0-.7-.3-1.5-.8-2.1l-16-17c-1.1-1-3.2-1.4-4.4-.3-1.2 1.1-1.2 3.3 0 4.4l11.3 11.9H3c-1.7 0-3 1.3-3 3s1.3 3 3 3h33.1l-11.3 11.9c-1 1-1.2 3.3 0 4.4 1.2 1.1 3.3.8 4.4-.3l16-17c.5-.5.8-1.1.8-1.9z"></path>
                  </svg>
                </span>
              </div>
            </button>
            <Courselist onSelectCourse={handleCourseSelect} />
          </div>
        ) : (
          <form onSubmit={handleSubmit}>
            {user.token.type === "T" ? (
              <>
                <input type="text" placeholder="Class Name" ref={nameRef} />
                <textarea
                  placeholder="Class Description"
                  ref={descriptionRef}
                />
                <button type="button" onClick={toggleCourseList}>
                  Select Course
                </button>
                <span>Selected Course: {selectedCourseTitle}</span>
                <button type="submit">Create Class</button>
              </>
            ) : (
              <>
                <input type="text" placeholder="Class Code" ref={nameRef} />
                <button type="submit">Join Class</button>
              </>
            )}
          </form>
        )}
      </div>
    </div>
  );
}

export default ClassModal;
