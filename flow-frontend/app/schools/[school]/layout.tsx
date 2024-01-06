import Link from 'next/link';

export default function SchoolLayout({ params }: { params: { school: string } }) {
    return (
        <div>
            <nav className="bg-gray-200 py-4">
                <ul className="flex space-x-4">
                    <li>
                        <Link href={`/schools/${params.school}/courses`}
                            className="text-gray-600 hover:text-gray-900">
                            Courses
                        </Link>
                    </li>
                    <li>
                        <Link href={`/schools/${params.school}/departments`}
                            className="text-gray-600 hover:text-gray-900">
                            Departments
                        </Link>
                    </li>
                </ul>
            </nav>
        </div>
    );
}
