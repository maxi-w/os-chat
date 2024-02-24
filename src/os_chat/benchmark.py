from .main import setup_assistant


def main():
    print("Start running os bench...")
    assistant = setup_assistant()
    
    benchmark_data = [
        ("What is my CPU model?", "i5-12400F"),
        ("What is my operating System?", "Ubuntu"),
        ("What GPU do I have?", "NVIDIA GeForce RTX 3060"),
    ]

    success_runs = 0
    for question, answer in benchmark_data:
        given_answer = assistant.run(question, stream=False)
        if answer in given_answer:
            success_runs += 1
            print(f"✅ {question}")
        else:
            print(f"❌ {question}")

    print(f"Success rate: {success_runs / len(benchmark_data)}")
        

if __name__ == "__main__":
    main()
