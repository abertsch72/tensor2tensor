# coding=utf-8
# Copyright 2022 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Extract references from CommonCrawl files."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tempfile

import utils
import wikisum

import tensorflow.compat.v1 as tf



flags = tf.flags
FLAGS = flags.FLAGS

flags.DEFINE_integer("num_tasks", 50, "Number of parallel tasks.")
flags.DEFINE_integer("task_id", 0, "Task id in a parallel run.")
flags.DEFINE_string("metadata_dir",
                    "gs://tensor2tensor-data/wikisum/commoncrawl_metadata/",
                    "Path to metadata files specifying what references are in "
                    "which CommonCrawl files.")
flags.DEFINE_string("out_dir", None, "Directory to write references to.")
flags.DEFINE_string("commoncrawl_wet_dir", "outputs/wet_dir",
                    "Path to CommonCrawl wet.gz files locally. If not "
                    "provided, will download.")


def main(task_id, out_dir, metadata_dir="outputs/commoncrawl_metadata/", num_tasks=1000, commoncrawl_wet_dir=None):

  out_dir = os.path.join(out_dir, "process_%d" % task_id)
  tf.gfile.MakeDirs(out_dir)

  with utils.timing("get_refs_commoncrawl"):
    # Get all WET files
    if commoncrawl_wet_dir:
      wet_files = tf.gfile.Glob(
          os.path.join(commoncrawl_wet_dir, "*.wet.gz"))
    else:
      tmp_dir = tempfile.gettempdir() + "/" +  str(task_id)
      if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
      wet_files = list(
          utils.wet_download_urls(utils.WET_PATHS_BY_DATE["0917"], tmp_dir))

    # Shard and select this task's work
    wet_files.sort()
    wet_files = utils.shard(wet_files, num_tasks)[task_id]
    tf.logging.info("Sharded out WET files. Processing %d files",
                    len(wet_files))

    wikisum.extract_references_from_wets(wet_files, metadata_dir, out_dir)


def call(id, out_dir):
  tf.logging.set_verbosity(tf.logging.INFO)
  main(id, out_dir)

if __name__ == "__main__":
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run()
