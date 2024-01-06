"use client";

import { useParams } from "next/navigation";
import { useEffect, useState } from "react";

type CourseData = {
  code: string;
  department: number;
  department_name: string;
  credits: string;
  description: string;
  extra?: string;
  lastUpdated: string;
  name: string;
  school: number;
  url: string;
};

const CoursePage: React.FC = () => {
  const { course, school, department } = useParams<{ school: string; department: string; course: string }>();
  const [data, setData] = useState<CourseData | null>(null);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/schools/${school}/departments/${department}/courses/${course}`)
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
        setLoading(false);
      });
  }, [course, school, department]);

  if (isLoading) return <p>Loading...</p>;
  if (!data) return <p>Course Not Found</p>;

  return (
    <div className="card">
      <h1>{data.code}</h1>
      <h2>{data.name}</h2>
      <h4>
        {data.department_name}, {data.credits}
      </h4>
      <p>{data.description}</p>
    </div>
  );
};

export default CoursePage;
