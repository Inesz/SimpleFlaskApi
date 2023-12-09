import time


class Timer:
    starts = []
    ends = []

    def start(self):
        self.starts.append(time.time())

    def stop(self):
        self.ends.append(time.time())

    def stop_no(self, no: int):
        self.ends[no] = time.time()

    def reset_all(self):
        self.starts = []
        self.ends = []

    def get_all(self) -> []:
        measurements = []
        for i in range(0, len(self.ends)):
            measurements.append(self.ends[i] - self.starts[i])
        return measurements

    def print_all(self, cols: int = 1):
        measurements = self.get_all()
        i = 0
        print("\n")

        while i < len(measurements)/cols:
            out = f"[{i}] | "
            for c in range(0, cols):
                out += f" [{c + 1}] = [{measurements[i * cols + c]}] |"
            print(out)
            i += 1

    def print_sum(self, cols: int = 1):
        measurements = self.get_all()
        i = 0
        sums = []

        for c in range(0, cols):
            sums.append(0)

        while i < len(measurements) - cols +1:
            for c in range(0, cols):
                sums[c] += measurements[i + c]
            i += cols

        out = "[sum] | "
        for c in range(0, cols):
            out += f" [{c + 1}] = [{sums[c]}] |"

        print(f"\n{out}")
