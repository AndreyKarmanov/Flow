type Faculty = {
  name: string;
  school: number;
  lastUpdated: string;
};

async function getData() {
  const res = await fetch("http://127.0.0.1:8000/api/schools/1/departments");

  if (!res.ok) {
    console.log("error");
  }

  return res.json();
}

export default async function Page() {
  const data = await getData();

  return (
    <main>
      <h1>Faculties</h1>
      {data && data.map((faculty: Faculty, index: number) => <h3 key={index}>{faculty.name}</h3>)}
    </main>
  );
}
