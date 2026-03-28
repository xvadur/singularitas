import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const execFileAsync = promisify(execFile);

export async function runCommand(command, args, options = {}) {
  try {
    const result = await execFileAsync(command, args, {
      maxBuffer: 25 * 1024 * 1024,
      ...options
    });

    return {
      stdout: result.stdout,
      stderr: result.stderr
    };
  } catch (error) {
    const detail = error.stderr || error.stdout || error.message;
    throw new Error(`Command failed: ${command} ${args.join(' ')}\n${detail}`);
  }
}
