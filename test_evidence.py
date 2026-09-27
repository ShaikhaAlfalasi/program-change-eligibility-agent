from evidence import build_evidence_package


def main():
    request_id = "YOUR_REQUEST_ID"

    evidence = build_evidence_package(request_id)

    print("\n=== EVIDENCE PACKAGE ===")

    print(f"\nRequest ID:")
    print(evidence["request_id"])

    print("\nCurrent Program:")
    print(evidence["current_program"])

    print("\nRequested Program:")
    print(evidence["requested_program"])

    print("\nRequested Program Study Plan:")
    requested_courses = (
        evidence["requested_program"]
        ["study_plan_source"]
        ["courses"]
    )

    for course in requested_courses:
        print(
            f"- {course['course_id']} | "
            f"{course['course_name']} | "
            f"{course['credit_hours']} credits"
        )

    print("\nTranscript:")
    for course in evidence["transcript"]:
        print(course)

    print("\nProgram Change Constraints:")
    print(evidence["program_change_constraints"])

    print("\nUniversity Courses:")
    print(evidence["university_courses"])

    print("\nSources:")
    for source in evidence["sources"]:
        print(source)


if __name__ == "__main__":
    main()